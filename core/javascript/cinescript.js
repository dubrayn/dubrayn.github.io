function CineScript(typescript, timing, options, container) {
    var FONTRATIO = 3;
    options = options || {};
    var self = this;

    var pre = document.createElement("pre");
    container.appendChild(document.createElement("tt").appendChild(pre));

    $(container).data("cinescript", self);

    //console.log("typescript: ..." + typescript + "...");
    var speed = (options['speed'] != null ? options['speed'] : 1);
    var cols = typeof options['cols'] !== 'undefined' ? options['cols'] : 80;
    var rows = typeof options['rows'] !== 'undefined' ? options['rows'] : 25;
    var autoplay = typeof options['autoplay'] !== 'undefined' ? options['autoplay'] : false;
    var showcontrols = (options['show-controls'] != null ? options['show-controls'] : true);
    var fontsize = (options['font-size'] != null ? options["font-size"] : "auto");

    speed = Math.max(+speed, 1);
    var orig_speed = 1;

    cols = +cols;
    rows = +rows;

    console.log("speed: " + speed);
    var FAST = 100;

    var terminal = new Terminal({cols: cols, rows: rows, screenKeys: false});
    terminal.open(pre);

    var timer = undefined;
    function Timer(callback, delay) {
        var timerId, start, remaining = delay;
        this.running = false;
        this.pause = function() {
            window.clearTimeout(timerId);
            remaining -= new Date() - start;
            this.running = false;
        };
        this.resume = function() {
            start = new Date();
            timerId = window.setTimeout(callback, remaining);
            this.running = true;
        };
        this.resume();
    }

    self.play = function() {
	if (self.toggleButton != undefined) {
            self.toggleButton.className = "cine-pause";
	}

        if (fontsize == "auto") {
            var new_size = Math.floor(FONTRATIO * $(container).width() / cols);
            if (new_size > 0) {
                fontsize = new_size + "px";
            }
        }
        //console.log("setting font-size to " + fontsize);
        $(container).css("font-size", fontsize);

        if (timer) {
            timer.resume();
            return;
        }

        var linenum = 0;
        var timings;
	if (timing != undefined) {
            timings = timing.split("\n");
	}
        else {
	    var where = 1;
            while (typescript[where - 1] != '\n') {
                where = where + 1;
            };
            for (var i=where; i< typescript.length - 1;i++) {
		var c = typescript[i];
		if (c == '\n') {
		    terminal.write('\r\n');
		}
		else {
                    terminal.write(c);
		}
	    }
	    return;
        }

        var text = "";

        var where = 1;
	while (typescript[where - 1] != '\n') {
            where = where + 1;
	};

        function next_line() {
            if (where < 0) {
                return;
            }
            //console.log("..." + text + "...");
            try {
                terminal.write(text);
            } catch(err) {
                console.log(err);
            }
	    
            var line = timings[linenum].split(" ");
            var time = parseFloat(line[0]);
            var bytes = parseInt(line[1]);
	    text = ''
	    var lbytes = bytes
            while (lbytes > 0) {

                function byteLength(str) {
                    // returns the byte length of an utf8 string
	            var s = str.length;
	            for (var i=str.length-1; i>=0; i--) {
	                var code = str.charCodeAt(i);
	                if (code > 0x7f && code <= 0x7ff) s++;
	                else if (code > 0x7ff && code <= 0xffff) s+=2;
	                if (code >= 0xDC00 && code <= 0xDFFF) i--; //trail surrogate
	            }
	            return s;
	        }

                text = text + typescript[where];
		lbytes = lbytes - byteLength(typescript[where]);
		where = where + 1;
	    }

            if (isFinite(time) && isFinite(bytes)) {
                //where += bytes;
                //console.log(linenum + " " + time + " " + bytes);
                linenum += 1;
                timer = new Timer(next_line, time*1000.0/speed);
            } else {
                text = typescript.slice(where);
                terminal.write(text);
                //terminal.write("\r*** done ***");
                where = -1; // finished
                timer = undefined;

                loop = true;

                if (loop) {
                  timer.pause();
                  timer = undefined;
                  terminal.reset();
                  self.play();
                }
                else {
	          if (self.toggleButton != undefined) {
                      self.toggleButton.className = "cine-play";
		  }
                }
            }
        }
        next_line();
    }

    self.pause = function() {
        if (self.toggleButton != undefined) {
            self.toggleButton.className = "cine-play";
	      }
        timer.pause();
    }

    self.toggle = function() {
        if (timer && timer.running) {
            self.pause();
        } else {
            self.play();
        }
    }


    self.restart = function() {
        if (timer) {
            timer.pause();
            timer = undefined;
        }
        terminal.reset();
        self.play();
    }

    self.skip = function() {
        if (speed < FAST) {
            speed = FAST;
        }
        else
        {
            speed = orig_speed;
        }

        console.log("new speed: " + speed);
        if (timer) {
            timer.resume();
        }
    }

    if ((showcontrols) && (timing != undefined)) {
        var overlay = document.createElement("div");
        overlay.className = "overlay";
        container.appendChild(overlay);

        var restart = document.createElement("i");
        restart.className = "cine-fast-backward";
        self.toggleButton = document.createElement("i");
        self.toggleButton.className = "cine-play";
        var fastforward = document.createElement("i");
        fastforward.className = "cine-fast-forward";

        var controls = document.createElement("span");
        controls.appendChild(restart);
        controls.appendChild(self.toggleButton);
        controls.appendChild(fastforward);

        overlay.appendChild(controls);
        $(restart).on('click', self.restart);
        $(self.toggleButton).on('click', self.toggle);
        $(fastforward).on('click', self.skip);
    }

    if ((autoplay) || (timing == undefined)) {
        self.play();
    }
    else
    {
      if (fontsize == "auto") {
        var new_size = Math.floor(FONTRATIO * $(container).width() / cols);
        if (new_size > 0) {
          fontsize = new_size + "px";
        }
      }
      //console.log("setting font-size to " + fontsize);
      $(container).css("font-size", fontsize);
    }

}


init_cinescripts = function() {
    $('[class="cinescript"]').each(function() {
        var container = this;
        var typescript_filename, timing_filename, options, data_dir;

	data_dir = this.getAttribute('data-dir');
	    

        typescript_filename = data_dir + '/typescript';
        timing_filename = data_dir + '/timeline';

        $.get(data_dir + '/dims', function(dims) {
            if (dims) {
		dims_lines = dims.split('\n')
                var line = dims_lines[0].split(" ");
                var rows = parseInt(line[0]);
                var cols = parseInt(line[1]);
		options['rows'] = rows;
		options['cols'] = cols;
            }
        }, "text");


        var options = {'autoplay': this.getAttribute('data-autoplay') || false};
        var lrows = this.getAttribute("data-rows");
	if (lrows != undefined) options['rows'] = lrows;
        var lcols = this.getAttribute("data-cols");
	if (lcols != undefined) options['cols'] = lcols;
        options['speed'] = this.getAttribute("data-speed") || "1";
        options['show-controls'] = this.getAttribute('data-show-controls') || "true";
        options['font-size'] = this.getAttribute('data-font-size') || '13px';

	var timing;
        $.get(timing_filename, function(ltiming) {
            if (ltiming) {
                timing = ltiming;
            }
        }, "text");

        $.get(typescript_filename, function(typescript) {
            if (typescript) {
                new CineScript(typescript, timing, options, container);
            }
        }, "text");
    });
};

trigger_cinescripts = function(event) {
    var cs_elements = $(event.currentSlide).find(".cinescript");
    if (cs_elements.length > 0) {
        for (var i=0; i<cs_elements.length; i++) {
            var cs_element = cs_elements[i];
            var cinescript = $(cs_element).data("cinescript");
            if (cinescript) {
                cinescript.restart();
            }
        };
    }
};


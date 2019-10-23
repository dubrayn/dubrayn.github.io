requirejs(["remark", "emojify", "mermaid", "katex.min", "auto-render.min"], function(remark2, emojify, mermaid, katex2, autorender) {
  // === Remark.js initialization ===
  var slideshow = remark.create({
    highlightStyle: 'monokai',
    countIncrementalSlides: false,
    highlightLines: false
  });

  // === Mermaid.js initialization ===
  mermaid.initialize({
    startOnLoad: false,
    cloneCssStyles: false,
    flowchart:{
      height: 50
    },
    sequenceDiagram:{
      width: 110,
      height: 30
    }
  });
  
  function initMermaid(s) {
    var diagrams = document.querySelectorAll('.mermaid');
    var i;
    for(i=0;i<diagrams.length;i++){
      if(diagrams[i].offsetWidth>0){
        mermaid.init(undefined, diagrams[i]);
      }
    }
  }
  
  slideshow.on('afterShowSlide', initMermaid);
  initMermaid(slideshow.getSlides()[slideshow.getCurrentSlideIndex()]);

  // === Emojify.js initialization ===
  emojify.run();

  // === KaTeX ===
  renderMathInElement(document.body,{delimiters: [{left: "$$", right: "$$", display: true}, {left: "\\(", right: "\\)", display: false}], ignoredTags: [] });

});

/*
requirejs(["katex.min", "auto-render.min"], function(katex_loaded) {
});
*/

/*
requirejs(["mermaid.js"         ], function(util) { });
requirejs(["term.js"            ], function(util) { });
requirejs(["jquery-2.1.1.min.js"], function(util) { });
requirejs(["extend-jquery.js"   ], function(util) { });
requirejs(["cinescript.js"      ], function(util) { });
requirejs(["gitgraph.js"        ], function(util) { });
*/

/*

// === Cinescript initialization ===
$(document).ready(init_cinescripts);

*/

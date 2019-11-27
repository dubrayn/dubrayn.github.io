/***********************
 *  CUSTOM TEMPLATES   *
 ***********************/

var myTemplateConfig = {
          colors: ["#30B030", "#0088c0", "#f1c109", "#c03020"],
          branch: {
            lineWidth: 5,
            spacingX: 45,
            labelRotation: 0
          },
          commit: {
            spacingY: -40,
            dot: {
              size: 7
            },
            message: {
              font: "normal 12pt Arial",
              displayAuthor: false,
              displayBranch: true,
              displayHash: false,
            }
          }
        };

var myTemplate = new GitGraph.Template(myTemplateConfig);

/***********************
 *    INITIALIZATION   *
 ***********************/

var configLarge = {
  template: myTemplate, // could be: "blackarrow" or "metro" or `myTemplate` (custom Template object)
  reverseArrow: false, // to make arrows point to ancestors, if displayed
  orientation: "vertical",
};

var configCompact = {
  template: myTemplate, // could be: "blackarrow" or "metro" or `myTemplate` (custom Template object)
  reverseArrow: false, // to make arrows point to ancestors, if displayed
  orientation: "vertical",
  mode: 'compact',
};

// ===== gitExample0 =====
cfg = configLarge;
cfg.elementId = 'gitExample0';
var g = new GitGraph(cfg);
var master = g.branch("master");
master.commit("Commit A");
g.tag("v0.1.0");
var dev = g.branch("dev");
dev.commit("Commit B");
dev.commit("Commit C");
master.checkout();
dev.merge();
g.tag("v0.2.0");
dev.checkout();
var fix1 = g.branch("fix1");
var fix2 = g.branch("fix2");
fix1.commit("Commit D");
fix1.commit("Commit E");
fix2.commit("Commit F");
fix1.commit("Commit G");
dev.checkout();
fix1.merge();
fix2.merge();
master.checkout();
dev.merge();
g.tag("v0.3.0");
dev.commit("Commit I");
master.checkout();
dev.merge();
g.tag("v0.4.0");
// ===== END =====

// ===== branchHowto0 =====
cfg = configLarge;
cfg.elementId = 'branchHowto0';
var g = new GitGraph(cfg);
var master = g.branch("master");
master.commit("Commit A");
master.commit("Commit B");
master.tag("v0.1.0");
master.commit("Commit C");
master.tag("v0.2.0");
// ===== END =====

// ===== branchHowto1 =====
cfg = configLarge;
cfg.elementId = 'branchHowto1';
var g = new GitGraph(cfg);
var master = g.branch("master");
master.commit("Commit A");
master.commit("Commit B");
master.tag("v0.1.0");
master.commit("Commit C");
master.tag("v0.2.0");
var newfunc = g.branch("newfunc");
newfunc.commit("Commit D");
newfunc.commit("Commit E");
newfunc.commit("Commit F");
// ===== END =====

// ===== branchHowto2 =====
cfg = configLarge;
cfg.elementId = 'branchHowto2';
var g = new GitGraph(cfg);
var master = g.branch("master");
master.commit("Commit A");
master.commit("Commit B");
master.tag("v0.1.0");
master.commit("Commit C");
master.tag("v0.2.0");
var newfunc = g.branch("newfunc");
newfunc.commit("Commit D");
newfunc.commit("Commit E");
newfunc.commit("Commit F");
// ===== END =====

// ===== branchHowto3 =====
cfg = configLarge;
cfg.elementId = 'branchHowto3';
var g = new GitGraph(cfg);
var master = g.branch("master");
master.commit("Commit A");
master.commit("Commit B");
master.tag("v0.1.0");
master.commit("Commit C");
master.tag("v0.2.0");
var newfunc = g.branch("newfunc");
newfunc.commit("Commit D");
newfunc.commit("Commit E");
newfunc.commit("Commit F");
var fixit = master.branch("fixit");
fixit.commit("Commit G");
fixit.commit("Commit H");
fixit.commit("Commit I");
fixit.commit("Fixed issue #627");
// ===== END =====

// ===== branchHowto4 =====
cfg = configLarge;
cfg.elementId = 'branchHowto4';
var g = new GitGraph(cfg);
var master = g.branch("master");
master.commit("Commit A");
master.commit("Commit B");
master.tag("v0.1.0");
master.commit("Commit C");
master.tag("v0.2.0");
var newfunc = g.branch("newfunc");
newfunc.commit("Commit D");
newfunc.commit("Commit E");
newfunc.commit("Commit F");
var fixit = master.branch("fixit");
fixit.commit("Commit G");
fixit.commit("Commit H");
fixit.commit("Commit I");
fixit.commit("Fixed issue #627");
// ===== END =====

// ===== branchHowto5 =====
cfg = configLarge;
cfg.elementId = 'branchHowto5';
var g = new GitGraph(cfg);
var master = g.branch("master");
master.commit("Commit A");
master.commit("Commit B");
master.tag("v0.1.0");
master.commit("Commit C");
master.tag("v0.2.0");
var newfunc = g.branch("newfunc");
newfunc.commit("Commit D");
newfunc.commit("Commit E");
newfunc.commit("Commit F");
var fixit = master.branch("fixit");
fixit.commit("Commit G");
fixit.commit("Commit H");
fixit.commit("Commit I");
fixit.commit("Fixed issue #627");
master.checkout();
fixit.merge();
master.tag("v0.2.1");
// ===== END =====

// ===== branchHowto6 =====
cfg = configLarge;
cfg.elementId = 'branchHowto6';
var g = new GitGraph(cfg);
var master = g.branch("master");
master.commit("Commit A");
master.commit("Commit B");
master.tag("v0.1.0");
master.commit("Commit C");
master.tag("v0.2.0");
var newfunc = g.branch("newfunc");
newfunc.commit("Commit D");
newfunc.commit("Commit E");
newfunc.commit("Commit F");
var fixit = master.branch("fixit");
fixit.commit("Commit G");
fixit.commit("Commit H");
fixit.commit("Commit I");
fixit.commit("Fixed issue #627");
master.checkout();
fixit.merge();
master.tag("v0.2.1");
// ===== END =====

// ===== branchHowto7 =====
cfg = configLarge;
cfg.elementId = 'branchHowto7';
var g = new GitGraph(cfg);
var master = g.branch("master");
master.commit("Commit A");
master.commit("Commit B");
master.tag("v0.1.0");
master.commit("Commit C");
master.tag("v0.2.0");
var newfunc = g.branch("newfunc");
newfunc.commit("Commit D");
newfunc.commit("Commit E");
newfunc.commit("Commit F");
var fixit = master.branch("fixit");
fixit.commit("Commit G");
fixit.commit("Commit H");
fixit.commit("Commit I");
fixit.commit("Fixed issue #627");
master.checkout();
fixit.merge();
master.tag("v0.2.1");
newfunc.checkout();
newfunc.commit("Commit J");
// ===== END =====

// ===== branchHowto8 =====
cfg = configLarge;
cfg.elementId = 'branchHowto8';
var g = new GitGraph(cfg);
var master = g.branch("master");
master.commit("Commit A");
master.commit("Commit B");
master.tag("v0.1.0");
master.commit("Commit C");
master.tag("v0.2.0");
var newfunc = g.branch("newfunc");
newfunc.commit("Commit D");
newfunc.commit("Commit E");
newfunc.commit("Commit F");
var fixit = master.branch("fixit");
fixit.commit("Commit G");
fixit.commit("Commit H");
fixit.commit("Commit I");
fixit.commit("Fixed issue #627");
master.checkout();
fixit.merge();
master.tag("v0.2.1");
newfunc.checkout();
newfunc.commit("Commit J");
master.checkout();
newfunc.merge();
master.tag("v0.3.0");
// ===== END =====

// ===== gitExample1 =====
cfg = configLarge;
cfg.elementId = 'gitExample1';
var g = new GitGraph(cfg);
var master = g.branch("master");
master.commit("Commit A");
g.tag("v0.1.0");
var dev = g.branch("dev");
dev.commit("Commit B");
dev.commit("Commit C");
master.checkout();
dev.merge();
g.tag("v0.2.0");
dev.checkout();
var fix1 = g.branch("fix1");
var fix2 = g.branch("fix2");
fix1.commit("Commit D");
fix1.commit("Commit E");
fix2.commit("Commit F");
fix1.commit("Commit G");
dev.checkout();
fix1.merge();
fix2.merge();
master.checkout();
dev.merge();
g.tag("v0.3.0");
dev.commit("Commit I");
master.checkout();
dev.merge();
g.tag("v0.4.0");
// ===== END =====

// ===== test00 =====
cfg = configLarge;
cfg.elementId = 'test00';
var g = new GitGraph(cfg);
var master = g.branch("master");
master.commit("Commit A");
g.tag("v0.1.0");
master.commit("Commit B");
// ===== END =====



This s where Netowrking meets OS. 

PF lessons:
  Pf stands for packet filtering.
  A group of pf rules lives in an anchor.
  An anchor file is best edited by nano anchor_name.txt.
  You can disable current pf rules with pfctl -d

Plist lesons:
  Plist are part of launch agents
  launch agents run when your computer is logged in.
  launch damoens run without you logged in.
  plist calls for soemthing to be executed by the launch agent.
  plist can only refer to one execution.
  To get around this you create a wrapper basically a script to execute more then one thing.
  Plist are written in xml.

Shell lessons:
  Shell scripts need you to almaost always list full path even if you are in that directory /path/to/fuel.sh
  If you are in the direcory you can write ./fuel.sh
  Check script permison with ls -l fuel.sh
  Add execution with chmod -x fuel.sh



$_ = "Today is Monday. I go to school on Friday.";print "變更前：$_\n";if(s/[MTWFS].{2,5}day/Thursday/g){    print "變更後：$_\n";}else{    print "無變更。\n";}
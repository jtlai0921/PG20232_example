$a = 0;

while($a < 8){
    if($a == 3){
        print "$a\n";
        $a = 10;
        redo;
    }
    print "$a\n";
}continue{ $a += 1; }

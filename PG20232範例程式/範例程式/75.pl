#顯示標題行
for($x = 2; $x < 8; $x++){
    print "16: 10: c | ";
}
print "\n";

#顯示線條
for($x = 2; $x < 8; $x++){
    print "----------+-";
}
print "\n";

#顯示資料
for($y = 0; $y < 16; $y++){
    for($x = 2; $x < 8; $x++){
        $c = $x * 16 + $y;
        printf("%X:%3d: %c | ", $c, $c, $c);
    }
    print "\n";
}
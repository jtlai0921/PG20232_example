$filename = "math.txt";$a = 10;$b = 5;open(FILE, ">" . $filename) || die "Error!\n";print FILE "加法：";printf (FILE "%d + %d = %d\n", $a, $b, $a + $b);print FILE "減法：";printf (FILE "%d - %d = %d\n", $a, $b, $a - $b);print "已對檔案「$filename」寫出。\n";close(FILE);
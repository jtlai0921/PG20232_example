sub swapval1{    $temp = $_[0];    $_[0] = $_[1];    $_[1] = $temp;}sub swapval2{    my ($x, $y) = @_;        $temp = $x;    $x = $y;    $y = $temp;}$a = 2; $b = 7;print "\$a = $a�A\$b = $b\n";&swapval1($a, $b);print "\$a = $a�A\$b = $b\n";&swapval2(*a, *b);print "\$a = $a�A\$b = $b\n";
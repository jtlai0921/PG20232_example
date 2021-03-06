$year = 2005;	#西元
$month = 6;	#月
$days = &getMonthDays($year, $month);	#日數

&printCalendar($year, $month, $days);

#--------------------------------------------------
# 日數的取得
#--------------------------------------------------
sub getMonthDays{
    local ($y, $m) = @_;
    
    if($m == 1 || $m == 3 || $m == 5 || $m == 7 ||
             $m == 8 || $m == 10 || $m == 12){
        return 31;
    }elsif($m == 4 || $m == 6 ||
             $m == 9 || $m == 11){
        return 30;
    }elsif($m == 2){
        if($y % 4 == 0 && $y % 100 != 0 || $y % 400 == 0){
            return 29;
        }else{
            return 28;
        }
    }else{
        return 0;
    }
}

#--------------------------------------------------
# 取得星期
# 傳回值0:Sun 1:Mon 2:Tue 3:Wed 4:Thu 5:Fri 6:Sat
#--------------------------------------------------
sub getWeekDay{
    my ($y, $m, $d) = @_;
    if($m == 1 || $m == 2){
        $y--;
        $m += 12;
    }
    
    #�c以Zeller公式計算星期
    my $w = ($y + int($y / 4) - int($y / 100)
             + int($y / 400) + int((13 * $m + 8) / 5) + $d) % 7;
    return $w;
}

#--------------------------------------------------
# 顯示月曆
#--------------------------------------------------
sub printCalendar{
    ($y, $m, $d) = @_;
    $week = &getWeekDay($y, $m, 1);
    
    print "\n        西元$y年$m月\n";
    print "-----------------------------\n";
    print " Sun Mon Tue Wed Thu Fri Sat\n";
    print "-----------------------------\n";

    for($i = 0; $i < $week; $i++){
        print "    ";
    }
    $w = $week;
    for($i = 1; $i <= $d; $i++){
        if($w % 7 == 0 && $w >= 6){
            print "\n";
        }
        printf("%4d", $i);
        $w++;
    }
}
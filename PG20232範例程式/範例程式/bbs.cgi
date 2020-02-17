#!/perl/bin/perl

#主程式===========
%input = ("TITLE"=>"無標題", "NAME"=>"沒有姓名");
$filename = "bbsData.txt";  #寫入資料的儲存檔
&getString();  #輸入資料的取得

print "Content-type: text/html\n\n";
print "<HTML><HEAD><TITLE>留言板</TITLE></HEAD>\n";
print "<BODY><CENTER>\n";

&pageForm();  #顯示輸入表單
&pageList();  #顯示寫入資料

print "</CENTER></BODY></HTML>\n";

#輸入資料的取得===========
sub getString{
  if($ENV{"REQUEST_METHOD"} eq "GET"){
    $str = $ENV{"QUERY_STRING"};
  }else{
    read(STDIN, $str, $ENV{"CONTENT_LENGTH"});
  }
  #解碼
  $str =~ tr/+/ /;
  $str =~ s/%([0-9A-Fa-f][0-9A-Fa-f])/pack("c", hex($1))/eg;
  
  #輸入資料的寫入
  foreach(split(/&/, $str)){
    my ($key, $value) = split(/=/, $_);
    $value =~ s/</&lt;/g;      #「<」的變換
    $value =~ s/>/&gt;/g;      #「>」的變換
    $value =~ s/\r\n/<BR>/g;   #換行的變換
    if($value ne ""){ $input{$key} = $value; }
  }
  #沒有輸入內容
  if($input{'COMMENT'} ne ""){
    #寫入檔案中
    open(FILE, ">>" . $filename) || die "Error!\n";
    print FILE "$input{'TITLE'}:::$input{'NAME'}:::$input{'COMMENT'}\n";
    close(FILE);
  }
}

#顯示輸入的表單===========
sub pageForm{
print << "EOF";
<FORM NAME="FORM" ACTION="bbs.cgi" METHOD="POST">
<FONT SIZE="+2">留言板</FONT>
<TABLE>
  <TR>
    <TD>姓名</TD>
    <TD><INPUT TYPE="TEXT" SIZE="30" NAME="NAME"></TD>
  </TR>
  <TR>
    <TD>標題</TD>
    <TD><INPUT TYPE="TEXT" SIZE="30" NAME="TITLE"></TD>
  </TR>
  <TR>
    <TD>內容<FONT COLOR="red">*</FONT></TD>
    <TD><TEXTAREA COLS="50" ROWS="5" NAME="COMMENT"></TEXTAREA></TD>
  </TR>
</TABLE>
<INPUT TYPE="SUBMIT" VALUE="寫入">
<INPUT TYPE="RESET" VALUE="清除">
</FORM>
EOF
}

#顯示寫入資料==========
sub pageList{
  #沒有檔案就結束
  unless(-e $filename){ return; }
  print "<HR>\n";
  print "<TABLE WIDTH=\400\ BORDER=\1\>\n";
  open(FILE, "<" . $filename) || die "Error!\n";
  while(<FILE>){
    chomp($_);
    my ($title, $name, $comment) = split(/:::/, $_);
    print "\t<TR><TD>$title&nbsp;$name</TD></TR>\n";
    print "\t<TR><TD>$comment</TD></TR>\n";
  }
  close(FILE);
  print "</TABLE>\n";
}

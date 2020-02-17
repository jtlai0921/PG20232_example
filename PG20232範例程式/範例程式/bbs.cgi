#!/perl/bin/perl

#�D�{��===========
%input = ("TITLE"=>"�L���D", "NAME"=>"�S���m�W");
$filename = "bbsData.txt";  #�g�J��ƪ��x�s��
&getString();  #��J��ƪ����o

print "Content-type: text/html\n\n";
print "<HTML><HEAD><TITLE>�d���O</TITLE></HEAD>\n";
print "<BODY><CENTER>\n";

&pageForm();  #��ܿ�J���
&pageList();  #��ܼg�J���

print "</CENTER></BODY></HTML>\n";

#��J��ƪ����o===========
sub getString{
  if($ENV{"REQUEST_METHOD"} eq "GET"){
    $str = $ENV{"QUERY_STRING"};
  }else{
    read(STDIN, $str, $ENV{"CONTENT_LENGTH"});
  }
  #�ѽX
  $str =~ tr/+/ /;
  $str =~ s/%([0-9A-Fa-f][0-9A-Fa-f])/pack("c", hex($1))/eg;
  
  #��J��ƪ��g�J
  foreach(split(/&/, $str)){
    my ($key, $value) = split(/=/, $_);
    $value =~ s/</&lt;/g;      #�u<�v���ܴ�
    $value =~ s/>/&gt;/g;      #�u>�v���ܴ�
    $value =~ s/\r\n/<BR>/g;   #���檺�ܴ�
    if($value ne ""){ $input{$key} = $value; }
  }
  #�S����J���e
  if($input{'COMMENT'} ne ""){
    #�g�J�ɮפ�
    open(FILE, ">>" . $filename) || die "Error!\n";
    print FILE "$input{'TITLE'}:::$input{'NAME'}:::$input{'COMMENT'}\n";
    close(FILE);
  }
}

#��ܿ�J�����===========
sub pageForm{
print << "EOF";
<FORM NAME="FORM" ACTION="bbs.cgi" METHOD="POST">
<FONT SIZE="+2">�d���O</FONT>
<TABLE>
  <TR>
    <TD>�m�W</TD>
    <TD><INPUT TYPE="TEXT" SIZE="30" NAME="NAME"></TD>
  </TR>
  <TR>
    <TD>���D</TD>
    <TD><INPUT TYPE="TEXT" SIZE="30" NAME="TITLE"></TD>
  </TR>
  <TR>
    <TD>���e<FONT COLOR="red">*</FONT></TD>
    <TD><TEXTAREA COLS="50" ROWS="5" NAME="COMMENT"></TEXTAREA></TD>
  </TR>
</TABLE>
<INPUT TYPE="SUBMIT" VALUE="�g�J">
<INPUT TYPE="RESET" VALUE="�M��">
</FORM>
EOF
}

#��ܼg�J���==========
sub pageList{
  #�S���ɮ״N����
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

#!/perl/bin/perl

if($ENV{"REQUEST_METHOD"} eq "GET"){
    $str = $ENV{"QUERY_STRING"};
}else{
    read(STDIN, $str, $ENV{"CONTENT_LENGTH"});
}
$str =~ tr/+/ /;
$str =~ s/%([0-9A-Fa-f][0-9A-Fa-f])/pack("c", hex($1))/eg;
foreach(split(/&/, $str)){
    my ($key, $value) = split(/=/, $_);
    $data{$key} = $value;
}

print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<HEAD><TITLE>WELCOME</TITLE></HEAD>\n";
print "<BODY>$data{'NAME'}¤p©j,Åwªï¥úÁ{!</BODY>\n";
print "</HTML>\n";

#!/perl/bin/perl

$str = $ENV{"QUERY_STRING"};

print << "EOF";
Content-type: text/html

<HTML>
<HEAD>
<TITLE>CGI</TITLE>
</HEAD>
<BODY>
已接收資料︰$str
</BODY>
</HTML>
EOF

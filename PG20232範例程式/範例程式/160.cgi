#!/perl/bin/perl

$str = $ENV{"QUERY_STRING"};

print << "EOF";
Content-type: text/html

<HTML>
<HEAD>
<TITLE>CGI</TITLE>
</HEAD>
<BODY>
�w������ơJ$str
</BODY>
</HTML>
EOF

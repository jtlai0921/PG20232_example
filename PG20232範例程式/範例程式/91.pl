$r = "I love cat and dog." =~ /love (.+) and (.+)./;
print $1 . "\n";
print $2 . "\n";
print $& . "\n";

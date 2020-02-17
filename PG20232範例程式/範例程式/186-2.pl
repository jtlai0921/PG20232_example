print "1\n";
eval{
    print "2\n";
    die "Error!\n";
    print "3\n";
};
print "4\n";

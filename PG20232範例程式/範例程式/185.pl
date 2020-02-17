$dirname = "test";
mkdir $dirname;
opendir(DIR, $dirname) || die "opendir Error!\n";

$filename = $dirname . "/test1.txt";
open(FILE, ">" . $filename) || die "open Error!\n";
close(FILE);

@alldir = readdir DIR;
foreach ( @alldir ) {
    if(($_ ne ".") && ($_ ne "..")){
        print "$_\n";
    }
}

closedir(DIR);
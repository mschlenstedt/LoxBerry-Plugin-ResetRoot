#!/usr/bin/perl

use LoxBerry::Web;
use LoxBerry::System;
my $plugintitle = "LoxBerry Reset Root V" . LoxBerry::System::pluginversion();
#my $helplink = "https://www.loxwiki.eu/x/-gA_Ag";
#my $helptemplate = "help.html";

LoxBerry::Web::lbheader($plugintitle, $helplink, $helptemplate);

my $template = HTML::Template->new(
    filename => "$lbptemplatedir/index.html",
    global_vars => 1,
    loop_context_vars => 1,
    die_on_bad_params => 0,
);

my $password;
if (-e "$lbpdatadir/newrootpassword") {
	open(FH, '<', "$lbpdatadir/newrootpassword");
	$password = <FH>;
	unlink ("$lbpdatadir/newrootpassword");
}

if ($password) {
	$template->param( 'PASSWORD', $password );
} else {
	$template->param( 'PASSWORD', '--> You have been warned. I cannot show you the password anymore. <--' );
}

print $template->output();

LoxBerry::Web::lbfooter();


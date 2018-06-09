#!/usr/bin/perl
#Scan WebShell for LAKE2
#Desc: A small tools that find webshell with perl, it can check ASP/PHP/JSP/ASP.Net script, enjoy hacking :-)
#Author: lakehu[TSRC]
#Date: 2013-10-30
#Version: 1.1.1

use File::Find;

#php webshell str
@php_code_array = (
  '\beval(\s|\/\*.*?\*\/)*\(\s*.*?\s*\)',
  '\bassert(\s|\/\*.*?\*\/)*\(\s*.*?\s*\)',
  '\bsystem(\s|\/\*.*?\*\/)*\(\s*.*?\s*\)',
  '\bpassthru(\s|\/\*.*?\*\/)*\(\s*.*?\s*\)',
  '\bexec(\s|\/\*.*?\*\/)*\(\s*.*?\s*\)',
  '\bpcntl_exec(\s|\/\*.*?\*\/)*\(\s*.*?\s*\)',
  '\bshell_exec(\s|\/\*.*?\*\/)*\(\s*.*?\s*\)',
  '\bpopen(\s|\/\*.*?\*\/)*\(\s*.*?\s*\)',
  '\bproc_open(\s|\/\*.*?\*\/)*\(\s*.*?\s*\)',
  '\bpreg_replace(\s|\/\*.*?\*\/)*\(\s*.*?\s*\)',
  '\bcreate_function(\s|\/\*.*?\*\/)*\(\s*.*?\s*\)',
  '\bob_start(\s|\/\*.*?\*\/)*\(\s*.*?\s*\)',
  '\barray_map(\s|\/\*.*?\*\/)*\(\s*.*?\s*\)',
  '`.*?`',
  '(include|include_once|require|require_once)(\s|\/\*.*?\*\/)*\(\s*.*?\$.*?\)',
  '(include|include_once|require|require_once)(\s|\/\*.*?\*\/)*\(?\s*[\'"].*?\.[^p][^h][^p]\w*?[\'"].*?\s*?;',
  '(phpspy|4ngel|wofeiwo|c99shell|webshell|php_nst|reDuh)',
  '\$[\w-_\'\\[\\]{}\.\$\*/|]+(\s|\/\*.*?\*\/)*\(.*?\)'
);

@asp_code_array = (
  ''
);

#asp.net webshell str 
@aspx_code_array = (
  ''
);

#jsp webshell str 
@jsp_code_array = (
  ''
);

if(@ARGV!=2){
  print "\n"; 
  print "* Simple Scan WebShell by lake2 [ TSRC ] \n"; 
  print "* know it then hack it !\n"; 
  print "* Usage: ScanWebShell.pl <Path> <Type> \n"; 
  print "* Type: 1 - PHP\n";
  print "        2 - ASP\n";
  print "        3 - ASP.Net\n";
  print "        4 - JSP\n";
  print "* TSRC Website: http:\\\\security.tencent.com\n";
  exit; 
}

my $postfix;
$postfix = '';
my @str_code;
if($ARGV[1]==1)
{
  $postfix = '\.php$';push(@str_code, @php_code_array);
}
elsif($ARGV[1]==2)
{
  print "NO PUBLIC! Do you used ASPSecurity ?\n";exit;
}
elsif($ARGV[1]==3)
{
  print "NO PUBLIC!\n";exit;
}
elsif($ARGV[1]==4)
{
  print "NO PUBLIC!\n";exit;
}
else
{
  print "ERROR: unkown type !\n";exit; 
}
#old Perl is not Switch -_-!! FucK !!!!
#switch($ARGV[1]){
#  case 0  { print "get out!\n";exit; }
#  case 1  { $postfix = '\.php$';push(@str_code, @php_code_array); }
#  case 2  { $postfix = '\.(asp|cdx|cer)$';push(@str_code, @asp_code_array); }
#  case 3  { $postfix = '\.aspx$';push(@str_code, @aspx_code_array); }
#  case 4  { $postfix = '\.jsp$';push(@str_code, @jsp_code_array); }
#  else  { print "ERROR: unkown type !\n";exit; }
#}
print "start scanning ..... \n-----------------\n";
$scan_path = $ARGV[0];
if(substr($scan_path, length($scan_path)-1, 1) ne "/"){$scan_path.="/";}
find(\&wanted, $scan_path);
print "----------------\ndone !\n ";

sub   wanted   {   
	if   (-f   $File::Find::name) {   
      if   ($File::Find::name=~/$postfix/i) {
        checkfile($File::Find::name);
      }
  }
}   

sub checkfile{
  my($filepath) = @_;
  my($content);
  $content = openfile($filepath);
  if($content ne ""){
    foreach $item (@str_code){
      if($content =~ /$item/is){ # fix bug : ig -> is, \s will contain \r\n
        print $filepath." -> ".$&."\n";
      }
    }
  }
}

sub openfile{
  my($filepath) = @_;
  my(@string);
  unless (open (MYFILE, $filepath)) {
    print ("[-]ERROR: open file $filepath fail !\n");
    return "";
	}
	@string= <MYFILE>;
	close(MYFILE);
  return join("", @string);
}
#!/usr/bin/php -f

<?php
$tags = "０１２３ＡＢＣＤＦＷＳ＼＂，．？＜＞｛｝［］＊＆＾％＃＠！～（）＋－｜：；";
print_r($tags."\n");
$tags = iconv('utf-8', 'gbk', $tags);
$tags = preg_replace('/\xa3([\xa1-\xfe])/e', 'chr(ord(\1)-0x80)', $tags);
$tags = iconv( 'gbk', 'utf-8', $tags);
print_r($tags);
?>

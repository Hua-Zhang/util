<?php
header("Content-type: text/plain; charset=utf-8");
$data_dir = "dir to data";
if (isset($_GET["name"])) {
        $data_file = $data_dir . $_GET["name"];
        readfile($data_file);
}
?>

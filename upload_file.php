<?php
//文件上传脚本，主要使用了move_uploaded_file函数
/* 
  //这一部分是用来做类型检查的，当只允许特定类型的文件进行上传时可以使用
	$allowedExts = array("gif", "jpeg", "jpg", "png");
	$temp = explode(".", $_FILES["file"]["name"]);
	$extension = end($temp);
	if (((($_FILES["file"]["type"] == "image/gif")
	 || ($_FILES["file"]["type"] == "image/jpeg")
	 || ($_FILES["file"]["type"] == "image/jpg")
	 || ($_FILES["file"]["type"] == "image/pjpeg")
	 || ($_FILES["file"]["type"] == "image/x-png")
	 || ($_FILES["file"]["type"] == "image/png"))
	 && in_array($extension, $allowedExts))
	 || ($_FILES["file"]["type"] == "text/plain")) {
 */ 
	if ($_FILES["file"]["name"] != "") { //不加任何类型检查，均允许上传，这是很危险的，但是我自己用，就先这样吧
		if ($_FILES["file"]["error"] > 0) {
			echo "Return Code: " . $_FILES["file"]["error"] . "<br>";
		} else {
			echo "Upload: " . $_FILES["file"]["name"] . "<br>";
			echo "Type: " . $_FILES["file"]["type"] . "<br>";
			echo "Size: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
			echo "Temp file: " . $_FILES["file"]["tmp_name"] . "<br>";
			if (file_exists("data/" . $_FILES["file"]["name"])) {
				echo $_FILES["file"]["name"] . " already exists. ";
			} else {
				move_uploaded_file($_FILES["file"]["tmp_name"], "data/" . $_FILES["file"]["name"]);
				echo "Stored in: " . "data/" . $_FILES["file"]["name"];
			}
		}
	} else {
		echo "Invalid file";
	}
?>


<html>
	<body>
		<form method="post" enctype="multipart/form-data">
			<label for="file">Filename:</label>
			<input type="file" name="file" id="file" /> 
			<br />
			<input type="submit" name="submit" value="Submit" />
		</form>

	</body>
</html>

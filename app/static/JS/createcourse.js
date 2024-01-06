document.getElementById("createcourse-btn").addEventListener("click", function(event) {
  event.preventDefault();

 var name = document.getElementById("name").value;
 var credit = parseInt(document.getElementById("credit").value, 0);
 var class_hour = parseInt(document.getElementById("class_hour").value, 0);
 var teacher = document.getElementById("teacher").value;
 var dept = document.getElementById("dept").value;
 var major = document.getElementById("major").value;
 var grade = document.getElementById("grade").value;
 var semester = document.getElementById("semester").value;
 var time = document.getElementById("time").value;
 var place = document.getElementById("place").value;
 var number = parseInt(document.getElementById("number").value, 0);
 var max_number = parseInt(document.getElementById("max_number").value, 0);
  var data = {
  "name": name,
  "credit": credit,
  "class_hour": class_hour,
  "teacher": teacher,
  "dept": dept,
  "major": major,
  "grade": grade,
  "semester": semester,
  "time": time,
  "place": place,
  "number": number,
  "max_number": max_number
};
  console.log(JSON.stringify(data));

  fetch("http://127.0.0.1:8000/course/add", {
    method: "POST",
    body: JSON.stringify(data),
    headers: new Headers({
      "Content-Type": "application/json"
    })
  })
  .then(res => res.json())
  .then(res => {
    console.log(res);
    // 在这里可以执行根据服务器响应而执行的逻辑
    if (res.msg == "添加成功") {
      window.location.href = "/";
    } else {
      alert(res.msg);
    }
  })
});

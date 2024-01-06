document.getElementById("register-btn").addEventListener("click", function(event) {
  event.preventDefault(); // 阻止按钮的默认提交行为

  // 在此处编写要执行的注册函数代码
  var no = document.getElementById("no").value;
  var password = document.getElementById("password").value;
  var name = document.getElementById("name").value;
  var sex = document.getElementById("sex").value; // 获取性别的值
  var grade = global.toString(); // 获取年级的值
  var dept = document.getElementById("dept").value; // 获取学院/部门的值
  var major = document.getElementById("major").value; // 获取专业的值
  var title = document.getElementById("title").value; // 获取职称的值
  var data = {
    "no": no,
    "password": password,
    "name": name,
    "sex": sex,
    "grade": grade,
    "dept": dept,
    "major": major,
    "title": title
  };
  console.log(JSON.stringify(data));

  fetch("http://127.0.0.1:8000/student/add", {
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
      window.location.href = "/register";
    } else {
      alert(res.msg);
    }
  })
});


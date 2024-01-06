const loginBtn = document.getElementById("login-btn");
const registerBtn = document.getElementById("register-btn");

loginBtn.addEventListener("click", function(event) {
  // 处理登录按钮点击事件的代码
  event.preventDefault(); // 阻止表单默认提交行为
  var no = document.getElementById("no").value;
  var password = document.getElementById("password").value;
  var rememberMeCheckbox = document.getElementById('rememberMeCheckbox');
  var data = {
      "no": no,
      "password": password
  }
  fetch("http://127.0.0.1:8000/student/login", {
      method: "POST",
      body: JSON.stringify(data),
      headers: new Headers({
          "Content-Type": "application/json"
      },)
  })
  .then(res => res.json())
  .then(res => {
      console.log(res);
      if (res.msg == "登录成功") {
          if (rememberMeCheckbox.checked) {
              localStorage.setItem('rememberMe', true);
              localStorage.setItem('no', no);
              localStorage.setItem('password', password);
              localStorage.setItem('name', res.user_info.name);
              localStorage.setItem('sex', res.user_info.sex)
              localStorage.setItem('title', res.user_info.title)
              localStorage.setItem('dept', res.user_info.dept)
              localStorage.setItem('major', res.user_info.major)
              localStorage.setItem('grade', res.user_info.grade)

          } else {
              localStorage.removeItem('rememberMe');
              localStorage.removeItem('username');
              localStorage.removeItem('password');
          }
           if (res.user_info.title == "admin") {
              window.location.href = "/allcourse";
          } else {
              window.location.href = "/";
          }
      } else {
          alert(res.msg);
      }
  })
});



registerBtn.addEventListener("click", function(event) {
  // 跳转到注册页面
    console.log("register");
    event.preventDefault();
    window.location.href = "register";
});




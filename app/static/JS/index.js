document.addEventListener('DOMContentLoaded', function() {
  // 检查本地存储中是否有记住我选项的状态
  if (localStorage.getItem('rememberMe') === 'true') {
    // 获取保存的用户信息
    var no = localStorage.getItem('no');
    console.log("no: " + no);
    var name = localStorage.getItem('name');
    var sex = localStorage.getItem('sex');
    var title = localStorage.getItem('title');
    var dept = localStorage.getItem('dept');
    var major = localStorage.getItem('major');
    var grade = localStorage.getItem('grade');

    // 加载登录信息
    var sexElement = document.getElementById('sex');
    var titleElement = document.getElementById('title');
    sexElement.textContent = sex;
    titleElement.textContent = title;
    document.getElementById('no').textContent = no;
    document.getElementById('name').textContent = name;
    if (sexElement.textContent === 'male') {
        sexElement.textContent = '男';
    } else {
        sexElement.textContent = '女';
    }
    if (titleElement.textContent === 'teacher') {
        titleElement.textContent = '老师';
    }
    document.getElementById('dept').textContent = dept;
    document.getElementById('major').textContent = major;
    document.getElementById('grade').textContent = grade;
  } else {
    // 未登录，跳转到登录页面
    window.location.href = "login";
  }
});

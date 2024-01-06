var returnBtn = document.getElementById("return-btn");
var changePasswordBtn = document.getElementById('change-password-btn');

returnBtn.onclick = function() {
    window.location.href = "http://127.0.0.1:8000/teacher";
};



 changePasswordBtn.onclick = function() {
  // 创建对话框容器
  var dialogContainer = document.createElement('div');
  dialogContainer.id = 'change-password-dialog';
  dialogContainer.style.position = 'fixed';
  dialogContainer.style.top = '50%';
  dialogContainer.style.left = '50%';
  dialogContainer.style.transform = 'translate(-50%, -50%)';
  dialogContainer.style.boxShadow = '0px 0px 10px rgba(0, 0, 0, 0.5)';
  dialogContainer.style.padding = '20px';
  dialogContainer.style.backgroundColor = '#fff';
  dialogContainer.style.borderRadius = '5px';

  // 创建表单元素
  var form = document.createElement('form');
  form.id = 'change-password-form';
  form.method = 'POST';
  form.action = '/student/update';

  // 创建表单项
  var newPasswordLabel = document.createElement('label');
  newPasswordLabel.textContent = 'New Password:';
  var newPasswordInput = document.createElement('input');
  newPasswordInput.type = 'password';
  newPasswordInput.name = 'password';
  newPasswordInput.required = true;

  var studentNoLabel = document.createElement('label');
  studentNoLabel.textContent = '学号/工号:';
  var studentNoInput = document.createElement('input');
  studentNoInput.type = 'text';
  studentNoInput.name = 'no';

  var nameLabel = document.createElement('label');
  nameLabel.textContent = '用户名:';
  var nameInput = document.createElement('input');
  nameInput.type = 'text';
  nameInput.name = 'name';

  var sexLabel = document.createElement('label');
  sexLabel.textContent = '性别:';
  var sexInput = document.createElement('input');
  sexInput.type = 'text';
  sexInput.name = 'sex';

  var gradeLabel = document.createElement('label');
  gradeLabel.textContent = '入学（职）年份:';
  var gradeInput = document.createElement('input');
  gradeInput.type = 'text';
  gradeInput.name = 'grade';

  var deptLabel = document.createElement('label');
  deptLabel.textContent = '院系:';
  var deptInput = document.createElement('input');
  deptInput.type = 'text';
  deptInput.name = 'dept';

  var majorLabel = document.createElement('label');
  majorLabel.textContent = '专业:';
  var majorInput = document.createElement('input');
  majorInput.type = 'text';
  majorInput.name = 'major';

  var titleLabel = document.createElement('label');
  titleLabel.textContent = '职称:';
  var titleInput = document.createElement('input');
  titleInput.type = 'text';
  titleInput.name = 'title';

  // 添加表单项到表单中
  form.appendChild(studentNoLabel);
  form.appendChild(studentNoInput);
  form.appendChild(nameLabel);
  form.appendChild(nameInput);
  form.appendChild(newPasswordLabel);
  form.appendChild(newPasswordInput);
  form.appendChild(sexLabel);
  form.appendChild(sexInput);
  form.appendChild(gradeLabel);
  form.appendChild(gradeInput);
  form.appendChild(deptLabel);
  form.appendChild(deptInput);
  form.appendChild(majorLabel);
  form.appendChild(majorInput);
  form.appendChild(titleLabel);
  form.appendChild(titleInput);

  // 添加提交按钮
  var submitButton = document.createElement('input');
  submitButton.type = 'submit';
  submitButton.value = '提交';
  form.appendChild(submitButton);

  // 添加取消按钮
  var cancelButton = document.createElement('button');
  cancelButton.type = 'button';
  cancelButton.textContent = '取消';
  cancelButton.onclick = function() {
    // 点击取消按钮时移除对话框
    dialogContainer.parentNode.removeChild(dialogContainer);
  };
  form.appendChild(cancelButton);

 // 创建style标签
var style = document.createElement('style');

// 添加css样式
style.innerHTML = `
  form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  label {
    margin-top: 10px;
    font-size: 10px;
  }
  input[type="password"],
  input[type="text"] {
    width: 300px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    margin-top: 5px;
  }
  input[type="submit"] {
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 16px;
    margin-top: 20px;
    cursor: pointer;
  }
  button[type="button"] {
    background-color: #f2f2f2;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 16px;
    margin-top: 10px;
    cursor: pointer;
  }
`;

// 将style标签添加到head元素中
document.head.appendChild(style);



  // 表单提交事件处理函数
  form.onsubmit = function(e) {
    e.preventDefault(); // 阻止默认的表单提交行为

    var xhr = new XMLHttpRequest();
    xhr.open("POST", form.action, true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        alert(response.msg);
      }
    };

    var formData = new FormData(form);
    var encodedData = new URLSearchParams(formData).toString();

    xhr.send(encodedData);
  };

  // 将表单添加到对话框容器中
  dialogContainer.appendChild(form);

  // 显示对话框
  document.body.appendChild(dialogContainer);
};



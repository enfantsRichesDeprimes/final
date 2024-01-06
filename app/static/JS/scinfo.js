var returnBtn = document.getElementById("return-btn");
var changeGradeBtn = document.getElementById('change-grade-btn');

returnBtn.onclick = function() {
    window.location.href = "http://127.0.0.1:8000/teacher";
};

document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault(); // 阻止表单默认提交行为

    var no = document.getElementById('no').value;

    // 创建一个XMLHttpRequest对象
    var xhr = new XMLHttpRequest();

    // 设置请求的方法和URL
    xhr.open('POST', '/sc/search_by_course_no');
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');

    // 监听加载完成事件
    xhr.addEventListener('load', function() {
        if (xhr.status >= 200 && xhr.status < 400) {
            var response = JSON.parse(xhr.responseText);

            // 清空表格内容
            document.getElementById('table-body').innerHTML = '';

            if (response.scs !== null) {
                // 将返回的数据动态生成表格行
                response.scs.forEach(function(sc) {
                    var newRow = document.createElement('tr');
                    newRow.innerHTML = `
                        <td>${sc.id}</td>
                        <td>${sc.student_id}</td>
                        <td>${sc.course_id}</td>
                        <td>${sc.grade}</td>
                    `;
                    document.getElementById('table-body').appendChild(newRow);
                });
                var totalCount = response.scs.length;
                document.getElementById('total-count').textContent = totalCount;
            } else {
                console.log(response.msg);
            }
        } else {
            console.error('Error:', xhr.statusText);
        }
    });

    // 监听错误事件
    xhr.addEventListener('error', function() {
        console.error('Request failed');
    });

    var data = {no: no};

    // 发送请求
    xhr.send(JSON.stringify(data));
});


changeGradeBtn.onclick = function() {
  // 创建对话框容器
  var dialogContainer = document.createElement('div');
  dialogContainer.id = 'change-grade-dialog';
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
  form.id = 'change-grade-form';
  form.method = 'POST';
  form.action = '/sc/update';

  // 创建表单项
// 创建表单项
var studentNoLabel = document.createElement('label');
studentNoLabel.textContent = '学号:';
var studentNoInput = document.createElement('input');
studentNoInput.type = 'text';
studentNoInput.name = 'student_no'; // 与后端表单类的字段名一致
studentNoInput.value = ''; // 添加默认值

var courseNoLabel = document.createElement('label');
courseNoLabel.textContent = '课程号:';
var courseNoInput = document.createElement('input');
courseNoInput.type = 'text';
courseNoInput.name = 'course_no'; // 与后端表单类的字段名一致
courseNoInput.value = ''; // 添加默认值

  var gradeLabel = document.createElement('label');
  gradeLabel.textContent = '成绩';
  var gradeInput = document.createElement('input');
  gradeInput.type = 'number';
  gradeInput.name = 'grade';

  // 添加表单项到表单中
  form.appendChild(studentNoLabel);
  form.appendChild(studentNoInput);
  form.appendChild(courseNoLabel);
  form.appendChild(courseNoInput);
  form.appendChild(gradeLabel);
  form.appendChild(gradeInput);

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
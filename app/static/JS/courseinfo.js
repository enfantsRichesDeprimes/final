var returnBtn = document.getElementById("return-btn");

returnBtn.onclick = function() {
    window.location.href = "http://127.0.0.1:8000/teacher";
};

document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault(); // 阻止表单默认提交行为

    var no = document.getElementById('no').value;

    // 创建一个XMLHttpRequest对象
    var xhr = new XMLHttpRequest();

    // 设置请求的方法和URL
    xhr.open('POST', '/course/search_by_teacher_no');
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');

    // 监听加载完成事件
    xhr.addEventListener('load', function() {
    if (xhr.status >= 200 && xhr.status < 400) {
        var response = JSON.parse(xhr.responseText);

        // 清空表格内容
        document.getElementById('table-body').innerHTML = '';

         // 将返回的数据动态生成表格行
         response.courses.forEach(course => {
            var newRow = document.createElement('tr');
            newRow.innerHTML = `
            <td>${course.no}</td>
            <td>${course.name}</td>
            <td>${course.credit}</td>
            <td>${course.class_hour}</td>
            <td>${course.teacher}</td>
            <td>${course.dept}</td>
            <td>${course.major}</td>
            <td>${course.grade}</td>
            <td>${course.semester}</td>
            <td>${course.time}</td>
            <td>${course.place}</td>
            <td>${course.number}</td>
            <td>${course.max_number}</td>
            `;
            document.getElementById('table-body').appendChild(newRow);
         });
         var totalCount = response.courses.length;
         document.getElementById('total-count').textContent = totalCount;
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
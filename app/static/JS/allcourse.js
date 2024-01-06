fetch('http://127.0.0.1:8000/course/search_all', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
})
  .then(response => response.json())
  .then(data => {
    if (data.msg === '查看成功') {
      var courses = data.courses;

      var courseTable = document.querySelector('table tbody');
      for (var i = 0; i < courses.length; i++) {
        var course = courses[i];
        var tr = document.createElement('tr');
        tr.innerHTML = `
          <td>${course.id}</td>
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
          <td>
            <button class="btn btn-primary w-100 py-2 mb-1" onclick="deleteCourse(${course.id})">删除</button>
          </td>
        `;
        courseTable.appendChild(tr);
      }
    } else {
      console.log('获取课程数据失败');
    }
  })
  .catch(error => {
    console.log('请求错误:', error);
  });

function deleteCourse(id) {
  if (window.confirm('确定要删除该课程吗？')) {
    fetch('http://127.0.0.1:8000/course/delete/'+ id, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        id: id
      })
    })
      .then(response => response.json())
      .then(data => {
        if (data.msg === '删除成功') {
          window.location.reload();
        } else {
          console.log('删除课程失败');
        }
      })
      .catch(error => {
        console.log('请求错误:', error);
      });
  } else {
    console.log('已取消删除');
  }
}

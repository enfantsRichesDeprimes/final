fetch('http://127.0.0.1:8000/student/search_all', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
})
  .then(response => response.json())
  .then(data => {
    if (data.msg === '查看成功') {
      var users = data.users;

      var userTable = document.querySelector('table tbody');
      for (var i = 0; i < users.length; i++) {
        var user = users[i];
        var tr = document.createElement('tr');
        tr.innerHTML = `
          <td>${user.id}</td>
          <td>${user.no}</td>
          <td>${user.name}</td>
          <td>${user.password}</td>
          <td>${user.sex}</td>
          <td>${user.grade}</td>
          <td>${user.dept}</td>
          <td>${user.major}</td>
          <td>${user.title}</td>
          <td>
            <button class="btn btn-primary w-100 py-2 mb-1" onclick="deleteUser(${user.id})">删除</button>
          </td>
        `;
        userTable.appendChild(tr);
      }
    } else {
      console.log('获取用户数据失败');
    }
  })
  .catch(error => {
    console.log('请求错误:', error);
  });

function deleteUser(id) {
  if (window.confirm('确定要删除该用户吗？')) {
    fetch('http://127.0.0.1:8000/student/delete/'+ id, {
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
          console.log('删除失败');
        }
      })
      .catch(error => {
        console.log('请求错误:', error);
      });
  } else {
    console.log('已取消删除');
  }
}

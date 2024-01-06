document.getElementById("searchsc-btn").addEventListener("click", function(event) {
    event.preventDefault();

    var student_id = document.getElementById("searchsc-input").value;

    fetch('http://127.0.0.1:8000/sc/search_sc/' + student_id, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
})
  .then(response => response.json())
  .then(data => {
    if (data.msg === '查看成功') {
      var scs = data.scs;

      var scTable = document.querySelector('table tbody');
      for (var i = 0; i < scs.length; i++) {
        var sc = scs[i];
        var tr = document.createElement('tr');
        tr.innerHTML = `
          <td>${sc.id}</td>
          <td>${sc.student_id}</td>
          <td>${sc.course_id}</td>
          <td>${sc.grade}</td>
          <td>
            <button class="btn btn-primary w-100 py-2 mb-1" onclick="deleteSc(${sc.id})">删除</button>
          </td>
        `;
        scTable.appendChild(tr);
      }
    } else {
      console.log('获取记录数据失败');
    }
  })
  .catch(error => {
    console.log('请求错误:', error);
  });
  });

function deleteSc(id) {
  if (window.confirm('确定要删除该记录吗？')) {
    fetch('http://127.0.0.1:8000/sc/deletesc/'+ id, {
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

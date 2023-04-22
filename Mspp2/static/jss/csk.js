

for (var i in parsedc) {
        x=document.getElementById("clist")
        x.innerHTML+=`<li type='1' class="list-group-item d-flex justify-content-between lh-condensed">
        <div>
            <h6 class="my-0">${parsedc[i]['name']}</h6>
            <small>${parsedc[i]['q']}</small>
        </div>
        <span class="text-muted">Rs${parsedc[i]['price']}</span>
    </li>`
}
var newparsedc=[]
for (var i in parsedc){ xc=[]
    for (var j in parsedc[i])
        xc.push(parsedc[i][j]); newparsedc.push(xc); xc=[];  }


document.getElementById("itemsk").value=JSON.stringify(newparsedc)
document.getElementById("item").value=JSON.stringify(neworderid)
localStorage.clear()
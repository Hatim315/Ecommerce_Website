document.querySelector('#thisc').addEventListener('click', function () {
    document.getElementById('mysidebar').style.width = "300px";
})
document.querySelector('#thisx').addEventListener('click', function () {
    document.getElementById('mysidebar').style.width = 0;
})
/*document.addEventListener('DOMContentLoaded', () => {
    $('.alert').alert()
})*/


// --------this is an object of cart item---------------------//
parsedc = JSON.parse(localStorage.getItem('cart'));
const neworderid = []

// ------------Update cart function-----------------------//upc = (cart) => {

upc = (cart) => {
    if (localStorage.getItem('cart') != null) {
        for (var i of Object.keys(parsedc)) {
            neworderid.push(parseInt(i.slice(2,)))
        }
        let sle = document.getElementById('per')
        for (var idd in cart) {
            sle.insertAdjacentHTML('afterend', `<li id="i${idd}" class=nanj>${
                cart[idd]['name']
            }${' '}<button id="p${idd}" class="bn plus">+</button><span id="v${idd}"> ${
                cart[idd]['q']
            } </span><button id="m${idd}" class="bn minus">-</button></li>`)
        }
        document.getElementById('cart').innerHTML = Object.keys(cart).length;
        localStorage.setItem('cart', JSON.stringify(cart))
    }
}
// ------------updated the cart gui after reload----------

upc(parsedc)
// --------------------Below function is for addition of cart---------------------------------//
let selectedplus = document.querySelectorAll(".plus");
let selectedminus = document.querySelectorAll(".minus");
plusthis = (cart) => {
    for (var i = 0, j = selectedplus.length; i < j; i++) {
        selectedplus[i].addEventListener('click', function () {
            thisid = this.id.toString().slice(1,)
            cart[thisid]['q'] += 1
            localStorage.setItem('cart', JSON.stringify(cart))
            document.getElementById('v' + thisid).innerHTML = cart[thisid]['q']

        })

    }
}
minusthis = (cart) => {
    for (var i = 0, j = selectedminus.length; i < j; i++) {
        selectedminus[i].addEventListener('click', function () {
            thisid = this.id.toString().slice(1,)
            cart[thisid]['q'] -= 1;
            cart[thisid]['q'] = Math.max(0, cart[thisid]['q'])
            if (cart[thisid]['q'] == 0) {
                document.getElementById('i' + thisid).remove();
                delete cart[thisid];
                localStorage.setItem('cart', JSON.stringify(cart))

            } else {
                localStorage.setItem('cart', JSON.stringify(cart))
                document.getElementById('v' + thisid).innerHTML = cart[thisid]['q']
            }
        })

    }
}
plusthis(parsedc)
minusthis(parsedc)

document.querySelector("#clearcart").addEventListener('click', function () {
    localStorage.removeItem('cart');
    document.getElementById('cart').innerText = 0;
    document.getElementById("mysidebar2").innerHTML = "";
    location.reload(true);
})

// ---------------------Below is hero function which activated when add to cart is pressed---------------------------------//
function hero(th) {
    if (localStorage.getItem("cart") == undefined) {
        var cart = {}

    } else {
        cart = JSON.parse(localStorage.getItem('cart'))
    }
    let idd = th.id.toString()
    if (cart[idd] == undefined) {
        cart[idd] = {
            name: document.getElementById('nam' + idd).innerHTML,
            q: 1,
            price: parseInt(document.getElementById("pri" + idd).innerHTML)
        };
        let sle = document.getElementById('per');
        sle.insertAdjacentHTML('afterend', `<li id="i${idd}" class=nanj>${
            cart[idd]['name']
        }${' '}<button id="p${idd}" class="bn plus">+</button><span id="v${idd}">${
            cart[idd]['q']
        }</span> <button id="m${idd}" class="bn minus">-</button></li>`);
       location.reload();


    }

    document.getElementById('cart').innerHTML = Object.keys(cart).length;
    localStorage.setItem('cart', JSON.stringify(cart));
}
// ------------------checkout--------------'//


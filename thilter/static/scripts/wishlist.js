let wishList =  getWishlistFromStorage()


if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}
const addWishlist = document.getElementById('add_wishlist')
const wishListCount = document.querySelectorAll('.custom_badge')
function updateWishListCount(count){
    wishListCount.forEach(element => {
        element.innerHTML = count
    })
}
let count = 0
function ready() {
    const removeCartItemButtons = document.getElementsByClassName('btn_danger')
    for (let i = 0; i < removeCartItemButtons.length; i++) {
        const button = removeCartItemButtons[i]
        button.addEventListener('click', removeCartItem)
    }
    const addToCartButtons = document.getElementsByClassName('shop-item-button')
    const fullLove = document.getElementById('add_wishlist')
    for (let i = 0; i < addToCartButtons.length; i++) {
        console.log('something')
        const button = addToCartButtons[i]
        button.addEventListener('click', addToCartClicked)
    }
    const clearAllBtn = document.querySelectorAll('.clear_btn')
    clearAllBtn.forEach(element => {
        element.addEventListener('click', () => {
            wishList.forEach(item => {
                const cartItems = document.querySelector('#cart-items')
                cartItems.innerHTML = ''
                removeFromWishlist(item.id)
            })
        })
    })
    wishList.forEach(item => {
        const button = document.querySelector(`#${item.id}`)
        if (button) {
            button.classList.remove('far')
            button.classList.add('fas')
        }

        addItemToCart(
            item.id, 
            item.title,
            item.price, 
            item.subPrice, 
            item.delivery, 
            item.imageSrc, 
            updateList=false
        )
    })

}
function removeCartItem(event) {
    const buttonClicked = event.target
    const target_id = buttonClicked.parentElement.getAttribute('target_id')
    buttonClicked.parentElement.parentElement.parentElement.remove()
    removeFromWishlist(target_id)
}


function addToCartClicked(event) {
    const button = event.target
    const shopItem = button.parentElement.parentElement
    const id = event.target.id;
    const title = shopItem.getElementsByClassName('shop-item-title')[0].innerText
    const price = shopItem.getElementsByClassName('shop-item-price')[0].innerText
    const subPrice = shopItem.getElementsByClassName('shop-item-subprice')[0].innerText
    const optDelivery = shopItem.getElementsByClassName('delivery_option')[0].innerText
    const imageSrc = shopItem.getElementsByClassName('shop-item-image')[0].src
    event.target.classList.remove('far')
    event.target.classList.add('fas')
    addItemToCart(id,title, price, subPrice, optDelivery, imageSrc)
}
function removeFromWishlist(target_id) {
    const target_element = document.querySelector(`#${target_id}`)
    if (target_element) {
        target_element.classList.remove('fas')
        target_element.classList.add('far')
    }
    count -= 1
    updateWishListCount(count)
    wishList = wishList.filter(element => element.id != target_id)
    storeWishlist()
}

function addItemToCart(id, title, price, subPrice, optDelivery, imageSrc, updateList=true) {
    const item = wishList.find(element => element.id == id)
    
    if (updateList) {
        if (item) {
            // Remove the item
            removeFromWishlist(id)
            document.querySelector(`#cart-items > .custom_wishlist_product[target_id='${id}']`).remove()
            return
        }

        wishList.push({
            'id': id,
            'title': title,
            'price': price,
            'subPrice' : subPrice,
            'imageSrc' : imageSrc,
            'delivery' : optDelivery
        })
    }

    const cartRow = document.createElement('div')
    cartRow.classList.add('col-md-4','custom_wishlist_product')
    cartRow.setAttribute('target_id', id)
    const cartItems = document.getElementsByClassName('cart-items')[0]
    const cartItemNames = cartItems.getElementsByClassName('cart-item-title')

    count += 1
    updateWishListCount(count)
    console.log(optDelivery)
    const cartRowContents = `
        <div class="custom_product cart-item text-center">
        <p class="custom_add_wishlist btn_danger" target_id=${id}><i class="fas fa-times custom_light"></i></p>
        <img src="${imageSrc}" class="img-fluid" width="45%" alt="" srcset="">
        <h2 class="pt-3 fs-5 text-capitalize cart-item-title">${title}</h2>
          <p class="custom_product_price">
            <span class="small_price">£</span>${price}<span class="small_price">${subPrice}</span></p>
          <p class="custom_delivery">${optDelivery}</p>
      </div>
        `
    cartRow.innerHTML = cartRowContents
    cartItems.append(cartRow)
    cartRow.getElementsByClassName('btn_danger')[0].addEventListener('click', removeCartItem)
    storeWishlist()
}

function getWishlistFromStorage() {
    const wishlist = localStorage.getItem('wishlist')
    if (wishlist)
        return JSON.parse(wishlist)
    else
        return []
}

function storeWishlist(){
    // Store to LocalStorage
    localStorage.setItem('wishlist', JSON.stringify(wishList))
}

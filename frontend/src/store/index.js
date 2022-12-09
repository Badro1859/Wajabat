import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex)

const store = new Vuex.Store ({
    state: {
        userID: 0,
        // cart: { items: [], },
        isAuthenticated: false,
        token: '',
        isLoading: false,
    },
    mutations: {
        initializeStore(state) {
        //     if (localStorage.getItem('cart')) {
        //         state.cart = JSON.parse(localStorage.getItem('cart'))
        //     } else {
        //         localStorage.setItem('cart', JSON.stringify(state.cart))
        //     }

            if (localStorage.getItem('token')) {
                state.token = localStorage.getItem('token')
                state.isAuthenticated = true
            } else {
                state.token = ''
                state.isAuthenticated = false
            }
        },
    // addToCart(state, item) {
    //     const exists = state.cart.items.filter(i => i.product.id === item.product.id)

    //     if (exists.length) {
    //         exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
    //     } else {
    //         state.cart.items.push(item)
    //     }

    //     localStorage.setItem('cart', JSON.stringify(state.cart))
    // },
    // clearCart(state) {
    //     state.cart = {
    //     items: []
    //     }
    //     localStorage.setItem('cart', JSON.stringify(state.cart))
    // },
    // setIsLoading(state, status) {
    //     state.isLoading = status
    // },

        setToken(state, token, id) {
            state.userID = id
            state.token = token
            state.isAuthenticated = true
        },
        removeToken(state) {
            state.userID = 0
            state.token = ''
            state.isAuthenticated = false
        }
    },
    actions: {
    },
    modules: {
    }
})

export default store;
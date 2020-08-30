var app = new Vue({
        el: '#app',
        data: {
            value: 0
        },
        methods: {
            generate: function () {
                eel.get_value()((val) => {
                  this.value = val
                })
            }
        }
    }
);
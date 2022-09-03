<template>
    <article>
        <form @submit.prevent="submit">
            <div class="form">
                <label>
                    お名前(姓)
                    <input v-model="formdata.last_name" type="text" required @focus="removeError('last_name')">
                </label>
                <label>
                    お名前(名)
                    <input v-model="formdata.first_name" type="text" required @focus="removeError('first_name')">
                </label>
            </div>

            <div class="form">
                <label>
                    ふりがな(姓)
                    <input v-model="formdata.ruby_last_name" type="text" required @focus="removeError('ruby_last_name')">
                </label>
                <label>
                    ふりがな(名)
                    <input v-model="formdata.ruby_first_name" type="text" required @focus="removeError('ruby_first_name')">
                </label>
            </div>

            <div class="form">
                <label>
                    メールアドレス
                    <input v-model="formdata.email" type="email" required @focus="removeError('email')" @blur="checkEmail">
                </label>
                <p v-if="error.email" class="error">⚠{{ error.email }}</p>
            </div>

            <div class="form">
                <label>
                    郵便番号から検索する(ハイフンなし)
                    <input v-model="zip" type="text" @input="findaddress">
                </label>
                <label>
                    都道府県・市区町村
                    <input v-model="formdata.address" type="text" required @focus="removeError('address')">
                </label>
            </div>

            <div class="form">
                <label>
                    ご年代
                    <select v-model="formdata.age" required>
                        <option value="0">10歳未満</option>
                        <option value="1">10代</option>
                        <option value="2">20代</option>
                        <option value="3">30代</option>
                        <option value="4">40代</option>
                        <option value="5">50代</option>
                        <option value="6">60代</option>
                        <option value="7">70代</option>
                        <option value="8">80歳以上</option>
                        
                    </select>
                </label>
            </div>

            <div class="form">
                <label>
                    ご職業
                    <select v-model="formdata.job" required>
                        <option value="未就学児">未就学児</option>
                        <option value="小学生">小学生</option>
                        <option value="中学生">中学生</option>
                        <option value="高校生">高校生</option>
                        <option value="大学生">大学生</option>
                        <option value="大学関係者">大学関係者</option>
                        <option value="会社員">会社員</option>
                        <option value="教職員">教職員</option>
                        <option value="自営業">自営業</option>
                        <option value="その他">その他</option>
                    </select>
                </label>
            </div>
        </form>
    </article>
</template>

<script>
export default {
    name: "RegistrationForm",
    data() {
        return {
            formdata: {
                last_name: "",
                first_name: "",
                ruby_last_name: "",
                ruby_first_name: "",
                email: "",
                address: "",
                age: "2",
                job: "大学生",
            },
            error: {
                last_name: "",
                first_name: "",
                ruby_last_name: "",
                ruby_first_name: "",
                email: "",
                address: "",
                age: "",
                job: "",
            },
            zip: "",
        }
    },
    methods: {
        submit() {

        },
        removeError(el) {
            this.error[el] = ""
        },
        checkEmail() {
            const match = this.formdata.email.match(/^[A-Za-z0-9]{1}[A-Za-z0-9_.-]*@{1}[A-Za-z0-9_.-]+\.[A-Za-z0-9]+$/)
            if (!match) {
                this.error.email = "正しいメールアドレスを入力してください"
            } else {
                this.error.email = ""
            }
        },
        findaddress() {
            if (this.zip.length === 7) {
                this.formdata.address = "検索中"
                this.$axios.get(`https://zipcloud.ibsnet.co.jp/api/search?zipcode=${this.zip}`)
                    .then(res => {
                        this.formdata.address = `${res.data.results[0].address1}${res.data.results[0].address2}`
                    })
            }
        }
    },
}
</script>

<style>
form {
    text-align: center;
    width: 80%;
    margin-left: auto;
    margin-right: auto;
}

.form {
    margin-top: 1em;
    margin-bottom: 1em;
}

.error {
    position: absolute;
    background-color: #ccc;
    padding: 5px;
    left: 50%;
    transform: translate(-50%, 5%);
    -webkit-transform: translate(-50%, 5%);
}

.error::before {
    content: '';
    position: absolute;
    left: 50%;
    transform: translate(-50%, -120%);
    -webkit-transform: translate(-50%, -120%);
    display: block;
    width: 0;
    height: 0;
    border-right: 15px solid transparent;
    border-bottom: 15px solid #ccc;
    border-left: 15px solid transparent;
}

input, select {
    border: solid 1px black;
}
</style>
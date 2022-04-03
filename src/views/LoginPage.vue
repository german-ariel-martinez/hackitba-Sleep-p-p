<template>
  <div>
    <LoginNavbar/>
    <div class="login-body">
      <div class="login-form">
        <div class="form">
          <div class="customForm">
            <div class="formTitle">Log in</div>
            <div class="formBody">
              <input class="formInput" type="text" placeholder="Enter username" v-model="username"/>
              <input class="formInput" type="password" placeholder="Enter password" v-model="password"/>
            </div>
            <div class="formButton">
              <button @click="submitLoginForm()">Submit</button>
            </div>
          </div>
        </div>
        <div class="info">
          <div class="infoTitle">Having any troubles?</div>
          <div class="textHolder">
            <div class="infoText">
              Make sure you enter the email and password you used when you created your accound. If you want you can <a href="/">recover your password</a>.
            </div>
            <div class="infoText">
              Want to be part of out community? If you want you can register your account! <a href="">Here</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LoginNavbar from '@/components/LoginNavbar.vue'
import axios from "axios"
export default {
  name: 'LoginPage',
  data(){
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitLoginForm() {
      axios.post("/login", 
                {"username":this.username, "password":this.password})
            .then((res) => { 
                              console.log('entre al then')
                              if(res.data.status == 1){
                              localStorage.username = this.username; 
                              this.$router.push({name:'HomePage'});
            }}).catch(error => {console.log(error);});
    },
  },
  components: {
      LoginNavbar,
  }
}
</script>

<style scoped>
  .textHolder {
    height: 70%;
    width: 95%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-content: center;
    border-bottom-style: solid;
    border-bottom-width: 1px;
    border-bottom-style: rgba(214, 160, 160, 0.2);
    margin-left: 5%;
  }
  .infoText {
    width: 95%;
    margin-top: 5%;
    text-align: justify;
  }
  .infoTitle {
    display: flex;
    flex-direction: row;
    width: 95%;
    height: 15%;
    margin-left: 5%;
    justify-content: center;
    align-items: center;
    font-size: 3vh;
    border-bottom-style: solid;
    border-bottom-width: 1px;
    border-bottom-style: rgba(0,0,0,.2);
  }
  .formInput {
    width: 95%;
    height: 20%;
    border-radius: 10px;
    border-style: solid;
    border-color: rgba(0, 0, 0, .2);
    padding-left: 1vw;
  }
  .formInput:first-child {
    margin-bottom: 5vh;
  }
  .formBody {
    height: 70%;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .formButton {
    height: 15%;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }
  .formButton button {
    height: 70%;
    width: 30%;
    border-radius: 15px;
    border-style: none;
    color: white;
    background-color: rgba(192, 32, 52, .7);
  }
  .formTitle {
    height: 15%;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    background-color: rgba(0, 0, 0, .1);
    align-items: center;
    font-size: 5vh;
    border-top-right-radius: 15px;
  }
  .customForm {
    width: 98%;
    height: 100%;
    border-left-style: solid;
    border-left-width: 2px;
    border-left-color: #c62034;
  }
  .form {
    height: 95%;
    width: 50%;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    margin-left: 2vh;
  }
  .info {
    height: 95%;
    width: 50%;
    border-left-style: solid;
    border-left-width: 1.5px;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
    margin-right: 2vh;
  }
  .login-form {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 60%;
    width: 70%;
    border-style: solid;
    border-width: 5px;
    border-color: #202844;
    border-radius: 15px;
  }
  .login-body {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 91vh;
    width: 100%;
  }
</style>
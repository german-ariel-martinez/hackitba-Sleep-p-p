<template>
  <div>
    <LoginNavbar/>
    <div class="login-body">
      <div class="login-form">
        <div class="form">
          <form action="submit" class="customForm">
            <div class="formTitle">Personal information</div>
            <div class="formBody">
              <input class="formInput" type="text" placeholder="Enter username">
              <input class="formInput" type="date" placeholder="Birthdate" style="padding-right:10px">
              <input class="formInput" type="text" placeholder="Enter email">
              <input class="formInput" type="text" placeholder="Enter password">
              <input class="formInput" type="text" placeholder="Confirm password">
            </div>
            <div class="formButton">
              <button type="button">Submit</button>
            </div>
          </form>
        </div>
        <div class="info">
          <div class="infoTitle">Additional information</div>
          <div class="textHolder">
            <input class="formInput" type="text" placeholder="LinkedIn account">
            <input class="formInput" type="text" placeholder="Personal website">
            <textarea rows="6" cols="50" class="textArea" placeholder="Description" wrap=""/>
          </div>
          <div class="textInfo"> These fields are optional. </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .textInfo {
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      height: 15%;
  }
  .textArea {
      width: 100%;
      border-radius: 10px;
      border-style: solid;
      border-color: rgba(0, 0, 0, .2);
      padding-left: 1vw;
      padding-top: 1vh;
      resize: none;
      margin-bottom: 1vh;
  }
  .addButton {
      font-size: 4vh;
      display: flex;
      flex-direction: row;
      justify-content: flex-start;
      align-items: center;
      width: 20%;
  }
  .addInput {
      display: flex;
      flex-direction: row;
      justify-content: flex-end;
      align-items: center;
      width: 100%;
      height: 20%;
      margin-right: 0;
  }
  .sameLine {
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      width: 100vh;
  }
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
    font-size: 5vh;
    border-bottom-style: solid;
    border-bottom-width: 1px;
    border-bottom-style: rgba(0,0,0,.2);
  }

  .formInput {
    width: 100%;
    height: 20%;
    border-radius: 10px;
    border-style: solid;
    border-color: rgba(0, 0, 0, .2);
    padding-left: 1vw;
    margin-bottom: 1vh;
  }
  .formInput:first-child {
    margin-bottom: 1vh;
    margin-top: 1vh;
  }
  .formInput:last-child {
    margin-bottom: 0;
  }
  .formBody {
    height: 70%;
    width: 97%;
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
    width: 97%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    font-size: 5vh;
    border-top-right-radius: 15px;
    border-bottom-style: solid;
    border-bottom-width: 1px;
  }
  .customForm {
    width: 98%;
    height: 100%;
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
    height: 70%;
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

<script>
// @ is an alias to /src
import LoginNavbar from '@/components/LoginNavbar.vue'
export default {
  name: 'LandingPage',
  components: {
      LoginNavbar,
  }
}
</script>
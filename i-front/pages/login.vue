<template>
  <v-main>
    <v-container fluid fill-height >
      <v-row align="center" justify="center">
        <v-col cols="12" sm="6">

          
          <v-card
            tyle="opacity: 0.9;"
            elevation=10
            max-width=400
          >
            <v-tabs
              v-model="tabs"
              centered
            >
            <v-tab
              v-for="n in 2"
              :key="n"
            >
              {{ titles[n-1] }}
            </v-tab>
            </v-tabs>
            <div v-if="tabs==0">
                      
              <v-card-text >
                <v-form v-model="valid">
                  <v-text-field
                    v-model="email"
                    label="E-mail"
                    required
                  ></v-text-field>

                  <v-text-field
                    :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                    :rules="[rules.required]"
                    :type="show ? 'text' : 'password'"
                    name="input-10-2"
                    label="Пароль"
                    v-model="password"                  
                    required
                    class="input-group--focused"
                    @click:append="show = !show"
                  ></v-text-field>
                </v-form>
              </v-card-text> 
              <v-card-actions class="pt-0">
                <v-spacer></v-spacer>
                  <v-btn 
                    outlined 
                    text
                    
                  >Войти</v-btn>
                <v-spacer></v-spacer>              
              </v-card-actions>
            </div> 
            <div v-if="tabs==1">   
              <v-card-text >
                <v-form v-model="valid">
                  <v-text-field
                    v-model="email"
                    :rules="[rules.emailRules]"
                    label="E-mail"
                    required
                  ></v-text-field>

                  <v-text-field
                    v-model="password"
                    :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                    :rules="[rules.required, rules.min]"
                    :type="show ? 'text' : 'password'"
                    name="input-10-2"
                    label="Пароль"
                    hint="Не менее 8 символов"
                    required
                    class="input-group--focused"
                    @click:append="show = !show"
                  ></v-text-field>
                  <v-text-field
                    v-model="confirmPassword"
                    :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                    :rules="[rules.required, rules.min]"
                    :type="show ? 'text' : 'password'"
                    name="input-10-2"
                    label="Повторите пароль"
                    required
                    class="input-group--focused"
                    @click:append="show = !show"
                  ></v-text-field>
                </v-form>
              </v-card-text> 
              <v-card-actions class="pt-0">
                <v-spacer></v-spacer>
                  <v-btn outlined text>
                    Зарегистрироваться
                  </v-btn>
                <v-spacer></v-spacer>              
              </v-card-actions>
            </div>

          </v-card>

        </v-col>
      </v-row>
    
    </v-container>
  </v-main>

</template>
<script>
  export default {
    layout: 'promo',
    data(){
      return {
        show: false,
        tabs: 0,
        email: null,
        password: null,
        confirmPassword: null,
        rules: {
          required: value => !!value || 'Required.',
          min: v => v != null && v.length >= 8 || 'Min 8 characters',
          emailRules: value => {
            const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            return pattern.test(value) || 'Неправильный e-mail.'
          },
        },
        titles: ['Вход', 'Регистрация'],
        valid: null
      }
    },
    methods: {

    }
  }
  
</script>
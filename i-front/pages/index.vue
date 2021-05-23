<template>

  <v-card s
    tyle="opacity: 0.9;"
    elevation = 10
  >
      <v-tabs
        v-model="tabs"
        centered
      >
        <v-tab
          v-for="n in 3"
          :key="n"
        >
          {{ titles[n] }}
        </v-tab>
      </v-tabs>

    <v-tabs-items v-model="tabs">
      <v-tab-item>
        <v-card flat>
          <v-card-text>


              <v-text-field
                label="Ссылка на пост"
                placeholder="instagram.com/p/BoeeKVxlrfH/"
                outlined
              ></v-text-field>

            <v-chip-group
              column
              multiple
            >
            <v-chip
              filter
              v-for="tag in tags"
              :key="tag"
            >
              {{ tag }}
            </v-chip>


            </v-chip-group>

            <v-card
              class="d-flex align-end flex-column"
              elevation="0"


            >

            <v-btn x-large class="d-flex align-end flex-column">
              Запуск
            </v-btn>
            </v-card>



          </v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-title class="headline">
            An awesome title
          </v-card-title>
          <v-card-text>
            <p>
              Duis lobortis massa imperdiet quam. Donec vitae orci sed dolor rutrum auctor. Vestibulum facilisis, purus nec pulvinar iaculis, ligula mi congue nunc, vitae euismod ligula urna in dolor. Praesent congue erat at massa.
            </p>

            <p>
              Aenean posuere, tortor sed cursus feugiat, nunc augue blandit nunc, eu sollicitudin urna dolor sagittis lacus. Pellentesque egestas, neque sit amet convallis pulvinar, justo nulla eleifend augue, ac auctor orci leo non est. Etiam sit amet orci eget eros faucibus tincidunt. Donec sodales sagittis magna.
            </p>

            <p class="mb-0">
              Ut leo. Suspendisse potenti. Duis vel nibh at velit scelerisque suscipit. Fusce pharetra convallis urna.
            </p>
          </v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-title class="headline">
            An even better title
          </v-card-title>
          <v-card-text>
            <p>
              Maecenas ullamcorper, dui et placerat feugiat, eros pede varius nisi, condimentum viverra felis nunc et lorem. Sed hendrerit. Maecenas malesuada. Vestibulum ullamcorper mauris at ligula. Proin faucibus arcu quis ante.
            </p>

            <p class="mb-0">
              Etiam vitae tortor. Curabitur ullamcorper ultricies nisi. Sed magna purus, fermentum eu, tincidunt eu, varius ut, felis. Aliquam lobortis. Suspendisse potenti.
            </p>
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </v-card>

</template>
<script>
  export default {
    data () {
      return {
        tags: [
        'Исключить масфолловеров',
        'Профили с кол. постов >10',
        'Подписчики',
        '3 победителя'
      ],
        titles: ['', 'Розыгрыш', 'Лайктаймы', 'Че то еще'],
        tabs: null,
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      }
    },
    layout: 'promo'
    // page component definitions
  }
</script>

import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    rtl: true,
    theme: { 
        dark: true ,
        themes: {
            dark: {
                primary: '#4577b5',
                secondary: '#b0bec5',
                accent: '#8c9eff',
                error: '#b71c1c',
            },
            light: {
                primary: '#6132a8',
                secondary: '#b0bec5',
                accent: '#8c9eff',
                error: '#b71c1c',
            },
      },
    },
});

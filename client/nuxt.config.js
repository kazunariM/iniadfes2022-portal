export default {
	ssr: true,
	// Target: https://go.nuxtjs.dev/config-target
	target: "server",

	// Global page headers: https://go.nuxtjs.dev/config-head
	head: {
		title: "INIAD-FES2022",
		meta: [{ charset: "utf-8" }, { name: "viewport", content: "width=device-width, initial-scale=1" }, { hid: "description", name: "description", content: "" }, { name: "format-detection", content: "telephone=no" }],
		link: [{ rel: "icon", type: "image/png", href: "/favicon.png" }],
	},

	// Global CSS: https://go.nuxtjs.dev/config-css
	css: [],

	// Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
	plugins: [],

	// Auto import components: https://go.nuxtjs.dev/config-components
	components: true,

	// Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
	buildModules: [
		// https://go.nuxtjs.dev/eslint
		"@nuxtjs/eslint-module",
		// https://go.nuxtjs.dev/tailwindcss
		"@nuxtjs/tailwindcss",
	],

	// Modules: https://go.nuxtjs.dev/config-modules
	modules: [
		// https://go.nuxtjs.dev/axios
		"@nuxtjs/axios",
		// https://go.nuxtjs.dev/pwa
		// "@nuxtjs/pwa",
		// https://github.com/nuxt-community/style-resources-module
		"@nuxtjs/style-resources",
		"cookie-universal-nuxt",
	],

	// Axios module configuration: https://go.nuxtjs.dev/config-axios
	axios: {
		// Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
		baseURL: process.browser ? process.env.FRONT_BASE_URL : process.env.BACKEND_BASE_URL,
		proxy: true,
	},

	proxy: {
		"/api/": { target: process.env.API_URL },
	},

	// PWA module configuration: https://go.nuxtjs.dev/pwa
	pwa: {
		manifest: {
			lang: "en",
		},
	},

	styleResources: {
		scss: ["~/assets/scss/_mixin.scss", "~/assets/scss/_breakpoint.scss"],
	},

	// Build Configuration: https://go.nuxtjs.dev/config-build
	build: {},

	publicRuntimeConfig: {
		API_URL: process.env.API_URL,
	},

	router: {
		extendRoutes(routes, resolve) {
			routes.push({
				name: "404error",
				path: "*",
				component: resolve("~/pages/404.vue"),
			})
		},
	},
}

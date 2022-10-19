export default {
	ssr: true,
	// Target: https://go.nuxtjs.dev/config-target
	target: "server",

	htmlAttrs: {
		lang: "ja",
	},

	// Global page headers: https://go.nuxtjs.dev/config-head
	head: {
		title: "INIAD-FES2022",
		meta: [
			{ charset: "utf-8" },
			{ name: "viewport", content: "width=device-width, initial-scale=1" },
			{ name: "format-detection", content: "telephone=no" },
			{ hid: "description", name: "description", content: "赤羽台キャンパス大学祭「赤羽台祭」2022/10/29(土)・30(日)に開催！来場者事前受付はこちらから！" },
			{ hid: "og:description", name: "og:description", content: "赤羽台キャンパス大学祭「赤羽台祭」2022/10/29(土)・30(日)に開催！来場者事前受付はこちらから！" },
			{ hid: "og:url", name: "og:url", content: "https://portal.iniadfes.com/" },
			{ hid: "og:type", name: "og:type", content: "website" },
			{ hid: "og:title", name: "og:title", content: "赤羽台祭 ポータルサイト 来場者事前受付中！" },
			{ hid: "og:site_name", name: "og:site_name", content: "赤羽台キャンパス 赤羽台祭" },
			{ hid: "og:image", name: "og:image", content: "https://portal.iniadfes.com/portal_iniadfes_com.png" },
			{ hid: "keywords", name: "keywords", content: "東洋大学,赤羽,大学祭,INIAD-FES,WELLB-FES,INIAD,WELLB,2022" },
			{ hid: "twitter:card", name: "twitter:card", content: "summary_large_image" },
		],
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
		"/api/": { target: process.env.FRONT_BASE_URL },
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

	router: {
		extendRoutes(routes, resolve) {
			routes.push({
				name: "404error",
				path: "*",
				component: resolve("~/pages/404.vue"),
			})
		},
	},

	watchOptions: { poll: true },

	hooks: {
		"vue-renderer:ssr:context": (renderContext) => {
			const cheerio = require("cheerio")
			const doc = cheerio.load(renderContext.nuxt)
			doc(`body script`).remove()
			renderContext.nuxt = doc.html()
		},
	},
}

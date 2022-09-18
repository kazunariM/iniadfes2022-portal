module.exports = {
	root: true,
	env: {
		browser: true,
		node: true,
	},
	parserOptions: {
		parser: "@babel/eslint-parser",
		requireConfigFile: false,
	},
	extends: ["@nuxtjs", "plugin:nuxt/recommended", "prettier"],
	plugins: [],
	rules: {
		indent: ["error", "tab"],
		"no-tabs": 0,
		"vue/html-indent": ["error", "tab"],
		"vue/script-indent": ["error", "tab"],
		quotes: [
			"error",
			"double",
			{
				avoidEscape: true,
				allowTemplateLiterals: true,
			},
		],
		semi: ["error", "never"],
		"no-dupe-class-members": ["error"],
		"standard/computed-property-even-spacing": "off",
		"function-paren-newline": ["off", { minItems: 5 }],
		"vue/multi-word-component-names": "off",
	},
}

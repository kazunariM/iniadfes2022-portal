<template>
	<div>
		<h1>来場者登録</h1>
		<p>内容をご確認ください。</p>
		<ConfirmComponent />
	</div>
</template>

<script>
import ConfirmComponent from "~/components/Registration/ConfirmComponent"
export default {
	components: { ConfirmComponent },
	layout: "portal",
}
</script>

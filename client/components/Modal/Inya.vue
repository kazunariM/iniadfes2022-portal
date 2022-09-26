<template>
	<transition name="modal" appear>
		<div class="modal__overlay">
			<div class="modal__window">
				<div class="modal__content">
					<p><img src="/OK.png" alt="いにゃー" /></p>
					<slot />
				</div>
			</div>
		</div>
	</transition>
</template>

<script>
export default {
	name: "Inya",
}
</script>

<style lang="scss" scoped>
.modal {
	&__overlay {
		display: flex;
		align-items: center;
		justify-content: center;
		position: fixed;
		z-index: 100;
		top: 0;
		left: 0;
		height: 100%;
		width: 100%;
		background: rgba(0, 0, 0, 0.7);
	}

	&__window {
		height: 90%;
		width: 90%;
		overflow: hidden;
	}

	&__content {
		height: 100%;
		padding: 30px;
		color: white;
		img {
			width: 50%;
		}
	}
}

.modal-enter-active,
.modal-leave-active {
	transition: opacity 0.4s;
	.modal__window {
		transition: opacity 0.4s, transform 0.4s;
	}
}
.modal-leave-active {
	transition: opacity 0.6s ease 0.4s;
}
.modal-enter,
.modal-leave-to {
	opacity: 0;
	.modal__window {
		opacity: 0;
		transform: translateX(-20px);
	}
}
</style>

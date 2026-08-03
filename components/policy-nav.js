class PolicyNav extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
    <!-- Navigation -->
    <nav class="fixed w-full z-50 glass-panel border-b-0 border-white/5 transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-20">
                <div class="flex-shrink-0">
                    <a href="index.html" class="flex items-center gap-3 focus-visible:ring-2 focus-visible:ring-indigo-500 focus-visible:outline-none rounded">
                        <div class="w-10 h-10 bg-indigo-600 rounded-lg flex items-center justify-center font-black text-xl tracking-tighter shadow-lg shadow-indigo-500/20">
                            AW
                        </div>
                        <span class="font-bold text-xl tracking-tighter uppercase hidden sm:block">A.N.W. FOUNDATIONS</span>
                    </a>
                </div>
                <div class="hidden md:block">
                    <a href="index.html" class="px-6 py-2.5 rounded-full text-sm font-semibold bg-white/5 hover:bg-white/10 border border-white/10 transition-all focus-visible:ring-2 focus-visible:ring-indigo-500 focus-visible:outline-none">
                        Back to Home
                    </a>
                </div>
            </div>
        </div>
    </nav>
        `;
    }
}
customElements.define('policy-nav', PolicyNav);

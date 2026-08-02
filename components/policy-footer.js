class PolicyFooter extends HTMLElement {
    connectedCallback() {
        const path = window.location.pathname;
        const page = path.split('/').pop() || 'index.html';

        const isPrivacy = page === 'privacy.html';
        const isTerms = page === 'terms.html';
        const isRefund = page === 'refund.html';

        const privacyClass = isPrivacy ? 'text-indigo-400' : 'text-slate-600';
        const termsClass = isTerms ? 'text-indigo-400' : 'text-slate-600';
        const refundClass = isRefund ? 'text-indigo-400' : 'text-slate-600';

        this.innerHTML = `
    <footer class="bg-[#030712] border-t border-white/5 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row justify-between items-center gap-6">
                <p class="text-slate-600 text-[10px] uppercase tracking-widest font-bold">
                    &copy; 2026 A.N.W. FOUNDATIONS LLC. ALL RIGHTS RESERVED.
                </p>
                <div class="flex gap-8">
                    <a href="privacy.html" class="${privacyClass} hover:text-white text-[10px] font-bold uppercase tracking-widest focus-visible:ring-2 focus-visible:ring-indigo-500 focus-visible:ring-offset-2 focus-visible:ring-offset-[#030712] focus-visible:outline-none rounded transition-colors">Privacy</a>
                    <a href="terms.html" class="${termsClass} hover:text-white text-[10px] font-bold uppercase tracking-widest focus-visible:ring-2 focus-visible:ring-indigo-500 focus-visible:ring-offset-2 focus-visible:ring-offset-[#030712] focus-visible:outline-none rounded transition-colors">Terms</a>
                    <a href="refund.html" class="${refundClass} hover:text-white text-[10px] font-bold uppercase tracking-widest focus-visible:ring-2 focus-visible:ring-indigo-500 focus-visible:ring-offset-2 focus-visible:ring-offset-[#030712] focus-visible:outline-none rounded transition-colors">Refund Policy</a>
                </div>
            </div>
        </div>
    </footer>
        `;
    }
}
customElements.define('policy-footer', PolicyFooter);

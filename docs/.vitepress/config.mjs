import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Grand Archives",
  description: "A Knowledge Base Site",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/markdown-examples' }
    ],

    sidebar: [
      {
        text: 'Java',
        items: [
          { text: '基本数据类型', link: '/Java/Basics/基本数据类型' },
          { text: '基本运算符', link: '/Java/Basics/基本运算符' },
          { text: '基本语句', link: '/Java/Basics/基本语句' },
          { text: '命名规范', link: '/Java/Basics/命名规范' },
          { text: 'Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})

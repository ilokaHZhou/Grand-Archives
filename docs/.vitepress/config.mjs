import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Grand Archives",
  description: "A Knowledge Base Site",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Java', link: '/Java/Basics/基本数据类型' }
    ],

    sidebar: [
      {
        text: 'Java',
        items: [
          { text: '基本数据类型', link: '/Java/Basics/基本数据类型' },
          { text: '运算符', link: '/Java/Basics/运算符' },
          { text: '修饰符', link: '/Java/Basics/修饰符' },
          { text: '基本语句', link: '/Java/Basics/基本语句' },
          { text: '命名规范', link: '/Java/Basics/命名规范' },
          { text: '文件处理I/O', link: '/Java/Basics/文件处理与输入输出' },
          { text: '数组', link: '/Java/Basics/数组' },

          { text: 'Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' }
        ]
      },
      {
        text: '数据结构',
        items: [
          {
            text: 'Collection', 
            items: [
              { text: 'List', link: '/Java/Data Structure/List' },
              { text: 'Map', link: '/Java/Data Structure/Map' },
              { text: '集合选择', link: '/Java/Data Structure/集合选择' },
            ]
          },
          { text: '数组', link: '/Java/Data-Structure/数组' },
          { text: '链表', link: '/Java/Data-Structure/链表' },
          { text: '二叉树', link: '/Java/Data-Structure/二叉树' },
          { text: '堆、栈、队列', link: '/Java/Data-Structure/堆、栈、队列' },
          { text: '哈希', link: '/Java/Data-Structure/哈希' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})

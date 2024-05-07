#!/usr/bin/env ruby

require 'optparse'

def parse_options(args)
  options = {
    patterns: [],
    word: false,
    invert: false,
    count: false,
    match: false,
    pattern: false # 正则模式
  }

  OptionParser.new do |opts|
    opts.banner = "Usage:  rgrep.rb [options] <filename> [pattern]"

    opts.on("-w", "--word", "Search for the whole word") do
      if options[:pattern]
        #puts "The --word and --pattern options cannot be used together."
        options[:pattern] = false # -p and -w and stay together
      end
      options[:word] = true
    end

    opts.on("-p", "--pattern", "Search with a pattern") do
      if options[:word]
        #puts "The --word and --pattern options cannot be used together."
        options[:word] = false
      end
      options[:pattern] = true
    end

    opts.on("-v", "--invert", "Invert match for a pattern") do
      options[:invert] = true
    end

    opts.on("-c", "--count", "Count the number of matching lines") do
      options[:count] = true
    end

    opts.on("-m", "--match", "Show only the matching part of the line") do
      options[:match] = true
    end
  end.parse!(args)

  #if args.empty? || (!options[:word] && !options[:pattern] && options[:patterns].empty?)

  if args.empty?|| args.length == 1
    puts "Missing required arguments"
    exit
  end

  # options[:pattern] = true unless options[:word] || options[:pattern]
  unless options[:invert] || options[:count] || options[:word] || options[:pattern]
    options[:pattern] = true
  end

  #options[:patterns] = args[1..-1].map { |arg| options[:word] ? /\b#{Regexp.escape(arg)}\b/ : Regexp.new(arg) }
  options[:patterns] = args[1..-1].map do |arg| # 修改了这一行
    if options[:word]
      /\b#{Regexp.escape(arg)}\b/
    else
      Regexp.new(arg)
    end
  end

  [options, args.first]
end










# 定义一个方法来处理给定选项的文件
def process_file(filename, options)
  count = 0
  File.foreach(filename) do |line|
    matches = options[:patterns].any? { |pattern| line.match(pattern) }
    next if options[:invert] == matches
    count += 1
    next if options[:count]

    if options[:match] && matches
      options[:patterns].each do |pattern|
        line.scan(pattern) { |match| puts match }
      end
    else
      puts line
    end
  end

  puts count if options[:count]
end

# 主脚本逻辑
options, filename = parse_options(ARGV)
process_file(filename, options)

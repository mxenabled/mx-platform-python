require "yaml"
config = ::YAML.load(::File.read("openapi/config.yml"))
major, minor, patch = config["packageVersion"].split(".")

case ARGV[0]
when "major"
  major = major.succ
  minor = 0
  patch = 0
when "minor"
  minor = minor.succ
  patch = 0
when "patch"
  patch = patch.succ
end

config["packageVersion"] = "#{major}.#{minor}.#{patch}"
::File.open("openapi/config.yml", 'w') { |file| ::YAML.dump(config, file) }
puts config["packageVersion"]
